"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeOrganizationsAccessOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.organization_status


class DescribeOrganizationsAccessOutput(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_cloudformation.types.organization_status.OrganizationStatus"
    ]
    """<p>Presents the status of the <code>OrganizationAccess</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeOrganizationsAccessOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import aws_sdk_cloudformation.types.organization_status

        aws_sdk_cloudformation.types.organization_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> DescribeOrganizationsAccessOutput:
    out: DescribeOrganizationsAccessOutput = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudformation.types.organization_status

        out["status"] = (
            aws_sdk_cloudformation.types.organization_status.deserialize_query(
                child_status
            )
        )
    return out
