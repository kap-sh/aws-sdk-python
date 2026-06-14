"""Generated from Smithy shape ``com.amazonaws.location#UpdateKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class UpdateKeyResponse(TypedDict):
    key_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:key/ExampleKey</code> </p> </li> </ul>"""
    key_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource.</p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the API key resource was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeyResponse) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyName"] = value["key_name"]
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateKeyResponse:
    out: UpdateKeyResponse = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("UpdateKeyResponse.key_arn required")
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("UpdateKeyResponse.key_name required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("UpdateKeyResponse.update_time required")
    return out
