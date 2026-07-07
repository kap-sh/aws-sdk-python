"""Generated from Smithy shape ``com.amazonaws.braket#InputFileConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.data_source
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.string256


class InputFileConfig(TypedDict, closed=True):
    channel_name: "aws_sdk_braket.types.string64.String64"
    """<p>A named input source that an Amazon Braket hybrid job can consume.</p>"""
    content_type: NotRequired["aws_sdk_braket.types.string256.String256"]
    """<p>The MIME type of the data.</p>"""
    data_source: "aws_sdk_braket.types.data_source.DataSource"
    """<p>The location of the input data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputFileConfig) -> dict:
    out: dict = {}
    out["channelName"] = value["channel_name"]
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    import aws_sdk_braket.types.data_source

    out["dataSource"] = aws_sdk_braket.types.data_source.serialize_json(
        value["data_source"]
    )
    return out


def deserialize_json(data: dict) -> InputFileConfig:
    out: InputFileConfig = {}  # type: ignore[typeddict-item]
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError("InputFileConfig.channel_name required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    if "dataSource" in data:
        import aws_sdk_braket.types.data_source

        out["data_source"] = aws_sdk_braket.types.data_source.deserialize_json(
            data["dataSource"]
        )
    else:
        raise DeserializationError("InputFileConfig.data_source required")
    return out
