"""Generated from Smithy shape ``com.amazonaws.finspace#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.data_bundle_arns
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_name
    import aws_sdk_finspace.types.federation_mode
    import aws_sdk_finspace.types.federation_parameters
    import aws_sdk_finspace.types.kms_key_id
    import aws_sdk_finspace.types.superuser_parameters
    import aws_sdk_finspace.types.tag_map


class CreateEnvironmentRequest(TypedDict, closed=True):
    name: "aws_sdk_finspace.types.environment_name.EnvironmentName"
    """<p>The name of the FinSpace environment to be created.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>The description of the FinSpace environment to be created.</p>"""
    kms_key_id: NotRequired["aws_sdk_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key id to encrypt your data in the FinSpace environment.</p>"""
    tags: NotRequired["aws_sdk_finspace.types.tag_map.TagMap"]
    """<p>Add tags to your FinSpace environment.</p>"""
    federation_mode: NotRequired[
        "aws_sdk_finspace.types.federation_mode.FederationMode"
    ]
    """<p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>"""
    federation_parameters: NotRequired[
        "aws_sdk_finspace.types.federation_parameters.FederationParameters"
    ]
    """<p>Configuration information when authentication mode is FEDERATED.</p>"""
    superuser_parameters: NotRequired[
        "aws_sdk_finspace.types.superuser_parameters.SuperuserParameters"
    ]
    """<p>Configuration information for the superuser.</p>"""
    data_bundles: NotRequired["aws_sdk_finspace.types.data_bundle_arns.DataBundleArns"]
    """<p>The list of Amazon Resource Names (ARN) of the data bundles to install. Currently supported data bundle ARNs:</p> <ul> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/capital-markets-sample</code> - Contains sample Capital Markets datasets, categories and controlled vocabularies.</p> </li> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/taq</code> (default) - Contains trades and quotes data in addition to sample Capital Markets data.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.serialize_json(value["tags"])
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
    if "superuser_parameters" in value:
        import aws_sdk_finspace.types.superuser_parameters

        out["superuserParameters"] = (
            aws_sdk_finspace.types.superuser_parameters.serialize_json(
                value["superuser_parameters"]
            )
        )
    if "data_bundles" in value:
        import aws_sdk_finspace.types.data_bundle_arns

        out["dataBundles"] = aws_sdk_finspace.types.data_bundle_arns.serialize_json(
            value["data_bundles"]
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.deserialize_json(data["tags"])
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
    if "superuserParameters" in data:
        import aws_sdk_finspace.types.superuser_parameters

        out["superuser_parameters"] = (
            aws_sdk_finspace.types.superuser_parameters.deserialize_json(
                data["superuserParameters"]
            )
        )
    if "dataBundles" in data:
        import aws_sdk_finspace.types.data_bundle_arns

        out["data_bundles"] = aws_sdk_finspace.types.data_bundle_arns.deserialize_json(
            data["dataBundles"]
        )
    return out
