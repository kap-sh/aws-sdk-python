"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Specifies the Auto-Tune state for the Elasticsearch domain. For valid states see the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a>.</p>"""
AutoTuneState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLE_IN_PROGRESS",
    "DISABLE_IN_PROGRESS",
    "DISABLED_AND_ROLLBACK_SCHEDULED",
    "DISABLED_AND_ROLLBACK_IN_PROGRESS",
    "DISABLED_AND_ROLLBACK_COMPLETE",
    "DISABLED_AND_ROLLBACK_ERROR",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLE_IN_PROGRESS",
        "DISABLE_IN_PROGRESS",
        "DISABLED_AND_ROLLBACK_SCHEDULED",
        "DISABLED_AND_ROLLBACK_IN_PROGRESS",
        "DISABLED_AND_ROLLBACK_COMPLETE",
        "DISABLED_AND_ROLLBACK_ERROR",
        "ERROR",
    )
)


def serialize_json(value: AutoTuneState) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoTuneState value: {data!r}")
    return cast(AutoTuneState, data)
