"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.endpoint

Endpoints: TypeAlias = list["aws_sdk_timestream_query.types.endpoint.Endpoint"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Endpoints) -> list:
    import aws_sdk_timestream_query.types.endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_timestream_query.types.endpoint.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Endpoints:
    import aws_sdk_timestream_query.types.endpoint

    out: Endpoints = []
    for item in data:
        out.append(
            aws_sdk_timestream_query.types.endpoint.deserialize_aws_json_1_0(item)
        )
    return out
