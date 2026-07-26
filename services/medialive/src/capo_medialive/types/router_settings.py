"""Generated from Smithy shape ``com.amazonaws.medialive#RouterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_router_destination_settings
    import capo_medialive.types.__string
    import capo_medialive.types.router_encryption_type


class RouterSettings(TypedDict, closed=True):
    destinations: NotRequired[
        "capo_medialive.types.__list_of_router_destination_settings.__listOfRouterDestinationSettings"
    ]
    """Destinations for the input from MediaConnect Router. Provide one for a single-pipeline input and two for a standard input."""
    encryption_type: NotRequired[
        "capo_medialive.types.router_encryption_type.RouterEncryptionType"
    ]
    secret_arn: NotRequired["capo_medialive.types.__string.__string"]
    """ARN of the secret used to encrypt this input."""


# --- restJson1 ser/de ---
def serialize_json(value: RouterSettings) -> dict:
    out: dict = {}
    if "destinations" in value:
        import capo_medialive.types.__list_of_router_destination_settings

        out["destinations"] = (
            capo_medialive.types.__list_of_router_destination_settings.serialize_json(
                value["destinations"]
            )
        )
    if "encryption_type" in value:
        import capo_medialive.types.router_encryption_type

        out["encryptionType"] = (
            capo_medialive.types.router_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> RouterSettings:
    out: RouterSettings = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import capo_medialive.types.__list_of_router_destination_settings

        out["destinations"] = (
            capo_medialive.types.__list_of_router_destination_settings.deserialize_json(
                data["destinations"]
            )
        )
    if "encryptionType" in data:
        import capo_medialive.types.router_encryption_type

        out["encryption_type"] = (
            capo_medialive.types.router_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    return out
