"""Generated from Smithy shape ``com.amazonaws.ec2#ExportVerifiedAccessInstanceClientConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.verified_access_instance_id


class ExportVerifiedAccessInstanceClientConfigurationRequest(TypedDict, closed=True):
    verified_access_instance_id: NotRequired[
        "capo_ec2.types.verified_access_instance_id.VerifiedAccessInstanceId"
    ]
    """<p>The ID of the Verified Access instance.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportVerifiedAccessInstanceClientConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ExportVerifiedAccessInstanceClientConfigurationRequest:
    out: ExportVerifiedAccessInstanceClientConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
