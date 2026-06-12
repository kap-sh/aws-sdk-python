"""Generated from Smithy shape ``com.amazonaws.route53domains#ListOperationsSortAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

ListOperationsSortAttributeName: TypeAlias = Literal["SubmittedDate",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SubmittedDate",))


def serialize_aws_json_1_1(value: ListOperationsSortAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListOperationsSortAttributeName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListOperationsSortAttributeName value: {data!r}"
        )
    return cast(ListOperationsSortAttributeName, data)
