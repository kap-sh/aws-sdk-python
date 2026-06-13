"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#PutMetadataFlagRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.put_metadata_flag_body


class PutMetadataFlagRequest(TypedDict):
    app_id: "str"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    feature_name: "str"
    """<p>The name of the feature associated with the metadata.</p>"""
    body: "aws_sdk_amplifyuibuilder.types.put_metadata_flag_body.PutMetadataFlagBody"
    """<p>The metadata information to store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMetadataFlagRequest) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.put_metadata_flag_body

    out["body"] = aws_sdk_amplifyuibuilder.types.put_metadata_flag_body.serialize_json(
        value["body"]
    )
    return out


def deserialize_json(data: dict) -> PutMetadataFlagRequest:
    out: PutMetadataFlagRequest = {}  # type: ignore[typeddict-item]
    if "body" in data:
        import aws_sdk_amplifyuibuilder.types.put_metadata_flag_body

        out["body"] = (
            aws_sdk_amplifyuibuilder.types.put_metadata_flag_body.deserialize_json(
                data["body"]
            )
        )
    else:
        raise DeserializationError("PutMetadataFlagRequest.body required")
    return out
