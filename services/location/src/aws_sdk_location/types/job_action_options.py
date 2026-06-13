"""Generated from Smithy shape ``com.amazonaws.location#JobActionOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.validate_address_action_options


class JobActionOptions(TypedDict):
    validate_address: NotRequired[
        "aws_sdk_location.types.validate_address_action_options.ValidateAddressActionOptions"
    ]
    """<p>Options specific to address validation jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobActionOptions) -> dict:
    out: dict = {}
    if "validate_address" in value:
        import aws_sdk_location.types.validate_address_action_options

        out["ValidateAddress"] = (
            aws_sdk_location.types.validate_address_action_options.serialize_json(
                value["validate_address"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobActionOptions:
    out: JobActionOptions = {}  # type: ignore[typeddict-item]
    if "ValidateAddress" in data:
        import aws_sdk_location.types.validate_address_action_options

        out["validate_address"] = (
            aws_sdk_location.types.validate_address_action_options.deserialize_json(
                data["ValidateAddress"]
            )
        )
    return out
