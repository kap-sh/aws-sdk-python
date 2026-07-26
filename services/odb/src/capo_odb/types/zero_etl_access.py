"""Generated from Smithy shape ``com.amazonaws.odb#ZeroEtlAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.managed_resource_status


class ZeroEtlAccess(TypedDict, closed=True):
    status: NotRequired["capo_odb.types.managed_resource_status.ManagedResourceStatus"]
    """<p>The status of the Zero-ETL access.</p>"""
    cidr: NotRequired["str"]
    """<p>The CIDR block for the Zero-ETL access.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ZeroEtlAccess) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_odb.types.managed_resource_status

        out["status"] = capo_odb.types.managed_resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ZeroEtlAccess:
    out: ZeroEtlAccess = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_odb.types.managed_resource_status

        out["status"] = capo_odb.types.managed_resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
