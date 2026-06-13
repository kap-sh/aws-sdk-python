"""Generated from Smithy shape ``com.amazonaws.omics#ShareDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.share_details

ShareDetailsList: TypeAlias = list["aws_sdk_omics.types.share_details.ShareDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareDetailsList) -> list:
    import aws_sdk_omics.types.share_details

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.share_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareDetailsList:
    import aws_sdk_omics.types.share_details

    out: ShareDetailsList = []
    for item in data:
        out.append(aws_sdk_omics.types.share_details.deserialize_json(item))
    return out
