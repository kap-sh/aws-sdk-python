"""Generated from Smithy shape ``com.amazonaws.opensearch#CognitoOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.cognito_options
    import aws_sdk_opensearch.types.option_status


class CognitoOptionsStatus(TypedDict):
    options: "aws_sdk_opensearch.types.cognito_options.CognitoOptions"
    """<p>Cognito options for the specified domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The status of the Cognito options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.cognito_options

    out["Options"] = aws_sdk_opensearch.types.cognito_options.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CognitoOptionsStatus:
    out: CognitoOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.cognito_options

        out["options"] = aws_sdk_opensearch.types.cognito_options.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("CognitoOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("CognitoOptionsStatus.status required")
    return out
