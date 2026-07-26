"""Generated from Smithy shape ``com.amazonaws.apprunner#TracingVendor``."""

from typing import Literal, TypeAlias, cast

TracingVendor: TypeAlias = Literal["AWSXRAY",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TracingVendor) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TracingVendor:
    return cast(TracingVendor, data)
