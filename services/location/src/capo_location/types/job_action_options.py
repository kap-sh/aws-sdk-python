"""Generated from Smithy shape ``com.amazonaws.location#JobActionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.validate_address_action_options


class JobActionOptions(TypedDict, closed=True):
    validate_address: NotRequired[
        "capo_location.types.validate_address_action_options.ValidateAddressActionOptions"
    ]
    """<p>Options specific to address validation jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobActionOptions) -> dict:
    out: dict = {}
    if "validate_address" in value:
        import capo_location.types.validate_address_action_options

        out["ValidateAddress"] = (
            capo_location.types.validate_address_action_options.serialize_json(
                value["validate_address"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobActionOptions:
    out: JobActionOptions = {}  # type: ignore[typeddict-item]
    if "ValidateAddress" in data:
        import capo_location.types.validate_address_action_options

        out["validate_address"] = (
            capo_location.types.validate_address_action_options.deserialize_json(
                data["ValidateAddress"]
            )
        )
    return out
