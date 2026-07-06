"""Generated from Smithy shape ``com.amazonaws.quicksight#NamespaceInfoV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.identity_store
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.namespace_error
    import aws_sdk_quicksight.types.namespace_status
    import aws_sdk_quicksight.types.string


class NamespaceInfoV2(TypedDict, closed=True):
    name: NotRequired["aws_sdk_quicksight.types.namespace.Namespace"]
    """<p>The name of the error.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The namespace ARN.</p>"""
    capacity_region: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The namespace Amazon Web Services Region.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.namespace_status.NamespaceStatus"
    ]
    """<p>The creation status of a namespace that is not yet completely created.</p>"""
    identity_store: NotRequired["aws_sdk_quicksight.types.identity_store.IdentityStore"]
    """<p>The identity store used for the namespace.</p>"""
    namespace_error: NotRequired[
        "aws_sdk_quicksight.types.namespace_error.NamespaceError"
    ]
    """<p>An error that occurred when the namespace was created.</p>"""
    iam_identity_center_application_arn: NotRequired[
        "aws_sdk_quicksight.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the IAM Identity Center application.</p>"""
    iam_identity_center_instance_arn: NotRequired[
        "aws_sdk_quicksight.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceInfoV2) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "capacity_region" in value:
        out["CapacityRegion"] = value["capacity_region"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.namespace_status

        out["CreationStatus"] = (
            aws_sdk_quicksight.types.namespace_status.serialize_json(
                value["creation_status"]
            )
        )
    if "identity_store" in value:
        import aws_sdk_quicksight.types.identity_store

        out["IdentityStore"] = aws_sdk_quicksight.types.identity_store.serialize_json(
            value["identity_store"]
        )
    if "namespace_error" in value:
        import aws_sdk_quicksight.types.namespace_error

        out["NamespaceError"] = aws_sdk_quicksight.types.namespace_error.serialize_json(
            value["namespace_error"]
        )
    if "iam_identity_center_application_arn" in value:
        out["IamIdentityCenterApplicationArn"] = value[
            "iam_identity_center_application_arn"
        ]
    if "iam_identity_center_instance_arn" in value:
        out["IamIdentityCenterInstanceArn"] = value["iam_identity_center_instance_arn"]
    return out


def deserialize_json(data: dict) -> NamespaceInfoV2:
    out: NamespaceInfoV2 = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CapacityRegion" in data:
        out["capacity_region"] = data["CapacityRegion"]
    if "CreationStatus" in data:
        import aws_sdk_quicksight.types.namespace_status

        out["creation_status"] = (
            aws_sdk_quicksight.types.namespace_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "IdentityStore" in data:
        import aws_sdk_quicksight.types.identity_store

        out["identity_store"] = (
            aws_sdk_quicksight.types.identity_store.deserialize_json(
                data["IdentityStore"]
            )
        )
    if "NamespaceError" in data:
        import aws_sdk_quicksight.types.namespace_error

        out["namespace_error"] = (
            aws_sdk_quicksight.types.namespace_error.deserialize_json(
                data["NamespaceError"]
            )
        )
    if "IamIdentityCenterApplicationArn" in data:
        out["iam_identity_center_application_arn"] = data[
            "IamIdentityCenterApplicationArn"
        ]
    if "IamIdentityCenterInstanceArn" in data:
        out["iam_identity_center_instance_arn"] = data["IamIdentityCenterInstanceArn"]
    return out
