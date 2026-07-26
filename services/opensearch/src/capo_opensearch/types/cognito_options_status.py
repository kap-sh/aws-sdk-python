"""Generated from Smithy shape ``com.amazonaws.opensearch#CognitoOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.cognito_options
    import capo_opensearch.types.option_status


class CognitoOptionsStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.cognito_options.CognitoOptions"
    """<p>Cognito options for the specified domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of the Cognito options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoOptionsStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.cognito_options

    out["Options"] = capo_opensearch.types.cognito_options.serialize_json(
        value["options"]
    )
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CognitoOptionsStatus:
    out: CognitoOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.cognito_options

        out["options"] = capo_opensearch.types.cognito_options.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("CognitoOptionsStatus.options required")
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("CognitoOptionsStatus.status required")
    return out
