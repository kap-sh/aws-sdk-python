"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Type of Log File, it can be one of the following: <ul> <li>INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than configured index query log threshold to execute.</li> <li>SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than configured search query log threshold to execute.</li> <li>ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.</li> <li>AUDIT_LOGS: Audit logs contain records of user requests for access from the domain.</li> </ul> </p>"""
LogType: TypeAlias = Literal[
    "INDEX_SLOW_LOGS",
    "SEARCH_SLOW_LOGS",
    "ES_APPLICATION_LOGS",
    "AUDIT_LOGS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDEX_SLOW_LOGS",
        "SEARCH_SLOW_LOGS",
        "ES_APPLICATION_LOGS",
        "AUDIT_LOGS",
    )
)


def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
