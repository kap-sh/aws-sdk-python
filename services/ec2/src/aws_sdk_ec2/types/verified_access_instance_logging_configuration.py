"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_logs


class VerifiedAccessInstanceLoggingConfiguration(TypedDict, closed=True):
    verified_access_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    access_logs: NotRequired[
        "aws_sdk_ec2.types.verified_access_logs.VerifiedAccessLogs"
    ]
    """<p>Details about the logging options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceLoggingConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "access_logs" in value:
        import aws_sdk_ec2.types.verified_access_logs

        aws_sdk_ec2.types.verified_access_logs.serialize_ec2_query(
            value["access_logs"], pairs, f"{prefix}.AccessLogs"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessInstanceLoggingConfiguration:
    out: VerifiedAccessInstanceLoggingConfiguration = {}  # type: ignore[typeddict-item]
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_access_logs = el.find("AccessLogs")
    if child_access_logs is not None:
        import aws_sdk_ec2.types.verified_access_logs

        out["access_logs"] = (
            aws_sdk_ec2.types.verified_access_logs.deserialize_ec2_query(
                child_access_logs
            )
        )
    return out
