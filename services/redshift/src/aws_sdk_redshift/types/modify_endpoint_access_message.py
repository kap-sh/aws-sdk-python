"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyEndpointAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.vpc_security_group_id_list


class ModifyEndpointAccessMessage(TypedDict, closed=True):
    endpoint_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The endpoint to be modified.</p>"""
    vpc_security_group_ids: NotRequired[
        "aws_sdk_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>The complete list of VPC security groups associated with the endpoint after the endpoint is modified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "endpoint_name" in value:
        pairs.append((f"{prefix}.EndpointName", str(value["endpoint_name"])))
    if "vpc_security_group_ids" in value:
        import aws_sdk_redshift.types.vpc_security_group_id_list

        aws_sdk_redshift.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{prefix}.VpcSecurityGroupIds"
        )


def deserialize_query(el: Element) -> ModifyEndpointAccessMessage:
    out: ModifyEndpointAccessMessage = {}  # type: ignore[typeddict-item]
    child_endpoint_name = el.find("EndpointName")
    if child_endpoint_name is not None:
        out["endpoint_name"] = str(child_endpoint_name.text or "")
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import aws_sdk_redshift.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            aws_sdk_redshift.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    return out
