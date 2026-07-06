"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerMonitoredTagKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class UpdateCapacityManagerMonitoredTagKeysRequest(TypedDict, closed=True):
    activate_tag_keys: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p> The tag keys to activate for monitoring. Once activated, these tag keys will be included as dimensions in capacity metric data. </p>"""
    deactivate_tag_keys: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p> The tag keys to deactivate. Deactivated tag keys will no longer be included as dimensions in capacity metric data. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateCapacityManagerMonitoredTagKeysRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "activate_tag_keys" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["activate_tag_keys"], pairs, f"{prefix}.ActivateTagKeys"
        )
    if "deactivate_tag_keys" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["deactivate_tag_keys"], pairs, f"{prefix}.DeactivateTagKeys"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> UpdateCapacityManagerMonitoredTagKeysRequest:
    out: UpdateCapacityManagerMonitoredTagKeysRequest = {}  # type: ignore[typeddict-item]
    if el.find("ActivateTagKeys") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["activate_tag_keys"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ActivateTagKeys"
            )
        )
    if el.find("DeactivateTagKeys") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["deactivate_tag_keys"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DeactivateTagKeys"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
