"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.compute_environment
    import aws_sdk_glue.types.name_string


class GetConnectionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the connection definition to retrieve.</p>"""
    hide_password: "aws_sdk_glue.types.boolean.Boolean"
    """<p>Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.</p>"""
    apply_override_for_compute_environment: NotRequired[
        "aws_sdk_glue.types.compute_environment.ComputeEnvironment"
    ]
    """<p>For connections that may be used in multiple services, specifies returning properties for the specified compute environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    out["HidePassword"] = value.get("hide_password", False)
    if "apply_override_for_compute_environment" in value:
        import aws_sdk_glue.types.compute_environment

        out["ApplyOverrideForComputeEnvironment"] = (
            aws_sdk_glue.types.compute_environment.serialize_aws_json_1_1(
                value["apply_override_for_compute_environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionRequest:
    out: GetConnectionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetConnectionRequest.name required")
    if "HidePassword" in data:
        out["hide_password"] = data["HidePassword"]
    else:
        out["hide_password"] = False
    if "ApplyOverrideForComputeEnvironment" in data:
        import aws_sdk_glue.types.compute_environment

        out["apply_override_for_compute_environment"] = (
            aws_sdk_glue.types.compute_environment.deserialize_aws_json_1_1(
                data["ApplyOverrideForComputeEnvironment"]
            )
        )
    return out
