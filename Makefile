csv-parse:
	@printf $(_TITLE) "INFO" "Voulez vous poursuivre ? [no / Yes]"
	@read -r line; \
	if [ $$line = "Yes" ]; then \
		printf $(_TITLE) "OK" "Continuing" ; \
		python3 main.py $(path) $(to);\
		exit 0; \
	else \
		printf $(_ERROR) "KO" "Stopping" ; \
		exit 0; \
	fi

.PHONY: csv-parse
_WARN := "\033[33m[%s]\033[0m %s\n"
_TITLE := "\033[32m[%s]\033[0m %s\n"
_ERROR := "\033[31m[%s]\033[0m %s\n"
