"""Generated from Smithy shape ``com.amazonaws.medialive#BatchDeleteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string


class BatchDeleteRequest(TypedDict, closed=True):
    channel_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of channel IDs"""
    input_ids: NotRequired["aws_sdk_medialive.types.__list_of__string.__listOf__string"]
    """List of input IDs"""
    input_security_group_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of input security group IDs"""
    multiplex_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of multiplex IDs"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRequest) -> dict:
    out: dict = {}
    if "channel_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["channelIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["channel_ids"]
        )
    if "input_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["inputIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["input_ids"]
        )
    if "input_security_group_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["inputSecurityGroupIds"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["input_security_group_ids"]
            )
        )
    if "multiplex_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["multiplexIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["multiplex_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteRequest:
    out: BatchDeleteRequest = {}  # type: ignore[typeddict-item]
    if "channelIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["channel_ids"] = aws_sdk_medialive.types.__list_of__string.deserialize_json(
            data["channelIds"]
        )
    if "inputIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["input_ids"] = aws_sdk_medialive.types.__list_of__string.deserialize_json(
            data["inputIds"]
        )
    if "inputSecurityGroupIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["input_security_group_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["inputSecurityGroupIds"]
            )
        )
    if "multiplexIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["multiplex_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["multiplexIds"]
            )
        )
    return out
