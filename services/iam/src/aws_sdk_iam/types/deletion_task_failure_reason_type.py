"""Generated from Smithy shape ``com.amazonaws.iam#DeletionTaskFailureReasonType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.reason_type
    import aws_sdk_iam.types.role_usage_list_type


class DeletionTaskFailureReasonType(TypedDict):
    reason: NotRequired["aws_sdk_iam.types.reason_type.ReasonType"]
    """<p>A short description of the reason that the service-linked role deletion failed.</p>"""
    role_usage_list: NotRequired[
        "aws_sdk_iam.types.role_usage_list_type.RoleUsageListType"
    ]
    """<p>A list of objects that contains details about the service-linked role deletion failure, if that information is returned by the service. If the service-linked role has active sessions or if any resources that were used by the role have not been deleted from the linked service, the role can't be deleted. This parameter includes a list of the resources that are associated with the role and the Region in which the resources are being used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletionTaskFailureReasonType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reason" in value:
        pairs.append((f"{prefix}.Reason", str(value["reason"])))
    if "role_usage_list" in value:
        import aws_sdk_iam.types.role_usage_list_type

        aws_sdk_iam.types.role_usage_list_type.serialize_query(
            value["role_usage_list"], pairs, f"{prefix}.RoleUsageList"
        )


def deserialize_query(el: Element) -> DeletionTaskFailureReasonType:
    out: DeletionTaskFailureReasonType = {}  # type: ignore[typeddict-item]
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    child_role_usage_list = el.find("RoleUsageList")
    if child_role_usage_list is not None:
        import aws_sdk_iam.types.role_usage_list_type

        out["role_usage_list"] = (
            aws_sdk_iam.types.role_usage_list_type.deserialize_query(
                child_role_usage_list
            )
        )
    return out
