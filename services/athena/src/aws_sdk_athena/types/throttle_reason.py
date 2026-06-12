"""Generated from Smithy shape ``com.amazonaws.athena#ThrottleReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

"""<p>The reason for the query throttling, for example, when it exceeds the concurrent query limit.</p>"""
ThrottleReason: TypeAlias = Literal["CONCURRENT_QUERY_LIMIT_EXCEEDED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONCURRENT_QUERY_LIMIT_EXCEEDED",))


def serialize_aws_json_1_1(value: ThrottleReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThrottleReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThrottleReason value: {data!r}")
    return cast(ThrottleReason, data)
