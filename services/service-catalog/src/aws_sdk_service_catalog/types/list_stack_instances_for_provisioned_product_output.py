"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListStackInstancesForProvisionedProductOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.stack_instances


class ListStackInstancesForProvisionedProductOutput(TypedDict):
    stack_instances: NotRequired[
        "aws_sdk_service_catalog.types.stack_instances.StackInstances"
    ]
    """<p>List of stack instances.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListStackInstancesForProvisionedProductOutput,
) -> dict:
    out: dict = {}
    if "stack_instances" in value:
        import aws_sdk_service_catalog.types.stack_instances

        out["StackInstances"] = (
            aws_sdk_service_catalog.types.stack_instances.serialize_aws_json_1_1(
                value["stack_instances"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListStackInstancesForProvisionedProductOutput:
    out: ListStackInstancesForProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if "StackInstances" in data:
        import aws_sdk_service_catalog.types.stack_instances

        out["stack_instances"] = (
            aws_sdk_service_catalog.types.stack_instances.deserialize_aws_json_1_1(
                data["StackInstances"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
