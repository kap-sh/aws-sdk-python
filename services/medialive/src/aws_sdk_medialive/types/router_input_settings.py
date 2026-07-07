"""Generated from Smithy shape ``com.amazonaws.medialive#RouterInputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_router_destination
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.router_encryption_type


class RouterInputSettings(TypedDict, closed=True):
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_router_destination.__listOfRouterDestination"
    ]
    """MediaConnect Router destinations associated with the MediaLive Input."""
    encryption_type: NotRequired[
        "aws_sdk_medialive.types.router_encryption_type.RouterEncryptionType"
    ]
    secret_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """ARN of the secret used to encrypt this input."""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputSettings) -> dict:
    out: dict = {}
    if "destinations" in value:
        import aws_sdk_medialive.types.__list_of_router_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_router_destination.serialize_json(
                value["destinations"]
            )
        )
    if "encryption_type" in value:
        import aws_sdk_medialive.types.router_encryption_type

        out["encryptionType"] = (
            aws_sdk_medialive.types.router_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> RouterInputSettings:
    out: RouterInputSettings = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_medialive.types.__list_of_router_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_router_destination.deserialize_json(
                data["destinations"]
            )
        )
    if "encryptionType" in data:
        import aws_sdk_medialive.types.router_encryption_type

        out["encryption_type"] = (
            aws_sdk_medialive.types.router_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    return out
