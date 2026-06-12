"""Generated from Smithy shape ``com.amazonaws.finspace#DataBundleArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.data_bundle_arn

DataBundleArns: TypeAlias = list["aws_sdk_finspace.types.data_bundle_arn.DataBundleArn"]


# --- restJson1 ser/de ---
def serialize_json(value: DataBundleArns) -> list:
    return list(value)


def deserialize_json(data: list) -> DataBundleArns:
    return list(data)
