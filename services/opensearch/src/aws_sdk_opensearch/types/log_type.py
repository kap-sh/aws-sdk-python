"""Generated from Smithy shape ``com.amazonaws.opensearch#LogType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of log file. Can be one of the following:</p> <ul> <li> <p> <b>INDEX_SLOW_LOGS</b> - Index slow logs contain insert requests that took more time than the configured index query log threshold to execute.</p> </li> <li> <p> <b>SEARCH_SLOW_LOGS</b> - Search slow logs contain search queries that took more time than the configured search query log threshold to execute.</p> </li> <li> <p> <b>ES_APPLICATION_LOGS</b> - OpenSearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.</p> </li> <li> <p> <b>AUDIT_LOGS</b> - Audit logs contain records of user requests for access to the domain.</p> </li> </ul>"""
LogType: TypeAlias = Literal[
    "INDEX_SLOW_LOGS",
    "SEARCH_SLOW_LOGS",
    "ES_APPLICATION_LOGS",
    "AUDIT_LOGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)
