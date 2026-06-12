"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The Auto-Tune state for the domain. For valid states see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html\">Auto-Tune for Amazon OpenSearch Service</a>. </p>"""
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
