"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_name
    import aws_sdk_finspace.types.federation_mode
    import aws_sdk_finspace.types.federation_parameters
    import aws_sdk_finspace.types.id_type


class UpdateEnvironmentRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>The identifier of the FinSpace environment.</p>"""
    name: NotRequired["aws_sdk_finspace.types.environment_name.EnvironmentName"]
    """<p>The name of the environment.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>The description of the environment.</p>"""
    federation_mode: NotRequired[
        "aws_sdk_finspace.types.federation_mode.FederationMode"
    ]
    """<p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>"""
    federation_parameters: NotRequired[
        "aws_sdk_finspace.types.federation_parameters.FederationParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "federation_mode" in value:
        import aws_sdk_finspace.types.federation_mode

        out["federationMode"] = aws_sdk_finspace.types.federation_mode.serialize_json(
            value["federation_mode"]
        )
    if "federation_parameters" in value:
        import aws_sdk_finspace.types.federation_parameters

        out["federationParameters"] = (
            aws_sdk_finspace.types.federation_parameters.serialize_json(
                value["federation_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentRequest:
    out: UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "federationMode" in data:
        import aws_sdk_finspace.types.federation_mode

        out["federation_mode"] = (
            aws_sdk_finspace.types.federation_mode.deserialize_json(
                data["federationMode"]
            )
        )
    if "federationParameters" in data:
        import aws_sdk_finspace.types.federation_parameters

        out["federation_parameters"] = (
            aws_sdk_finspace.types.federation_parameters.deserialize_json(
                data["federationParameters"]
            )
        )
    return out
