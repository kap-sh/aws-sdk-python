"""Generated from Smithy shape ``com.amazonaws.ec2#StartInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.string


class StartInstancesRequest(TypedDict):
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the instances.</p>"""
    additional_info: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_ids" in value:
        import aws_sdk_ec2.types.instance_id_string_list

        aws_sdk_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "additional_info" in value:
        pairs.append((f"{prefix}.AdditionalInfo", str(value["additional_info"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> StartInstancesRequest:
    out: StartInstancesRequest = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIds") is not None:
        import aws_sdk_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            aws_sdk_ec2.types.instance_id_string_list.deserialize_ec2_query(
                el, "InstanceIds"
            )
        )
    child_additional_info = el.find("AdditionalInfo")
    if child_additional_info is not None:
        out["additional_info"] = str(child_additional_info.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
