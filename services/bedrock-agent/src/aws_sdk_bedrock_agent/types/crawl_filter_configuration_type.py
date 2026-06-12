"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CrawlFilterConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

CrawlFilterConfigurationType: TypeAlias = Literal["PATTERN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PATTERN",))


def serialize_json(value: CrawlFilterConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> CrawlFilterConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CrawlFilterConfigurationType value: {data!r}"
        )
    return cast(CrawlFilterConfigurationType, data)
