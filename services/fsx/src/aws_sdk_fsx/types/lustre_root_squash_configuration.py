"""Generated from Smithy shape ``com.amazonaws.fsx#LustreRootSquashConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.lustre_no_squash_nids
    import aws_sdk_fsx.types.lustre_root_squash


class LustreRootSquashConfiguration(TypedDict, closed=True):
    root_squash: NotRequired["aws_sdk_fsx.types.lustre_root_squash.LustreRootSquash"]
    """<p>You enable root squash by setting a user ID (UID) and group ID (GID) for the file system in the format <code>UID:GID</code> (for example, <code>365534:65534</code>). The UID and GID values can range from <code>0</code> to <code>4294967294</code>:</p> <ul> <li> <p>A non-zero value for UID and GID enables root squash. The UID and GID values can be different, but each must be a non-zero value.</p> </li> <li> <p>A value of <code>0</code> (zero) for UID and GID indicates root, and therefore disables root squash.</p> </li> </ul> <p>When root squash is enabled, the user ID and group ID of a root user accessing the file system are re-mapped to the UID and GID you provide.</p>"""
    no_squash_nids: NotRequired[
        "aws_sdk_fsx.types.lustre_no_squash_nids.LustreNoSquashNids"
    ]
    """<p>When root squash is enabled, you can optionally specify an array of NIDs of clients for which root squash does not apply. A client NID is a Lustre Network Identifier used to uniquely identify a client. You can specify the NID as either a single address or a range of addresses:</p> <ul> <li> <p>A single address is described in standard Lustre NID format by specifying the client’s IP address followed by the Lustre network ID (for example, <code>10.0.1.6@tcp</code>).</p> </li> <li> <p>An address range is described using a dash to separate the range (for example, <code>10.0.[2-10].[1-255]@tcp</code>).</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreRootSquashConfiguration) -> dict:
    out: dict = {}
    if "root_squash" in value:
        out["RootSquash"] = value["root_squash"]
    if "no_squash_nids" in value:
        import aws_sdk_fsx.types.lustre_no_squash_nids

        out["NoSquashNids"] = (
            aws_sdk_fsx.types.lustre_no_squash_nids.serialize_aws_json_1_1(
                value["no_squash_nids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LustreRootSquashConfiguration:
    out: LustreRootSquashConfiguration = {}  # type: ignore[typeddict-item]
    if "RootSquash" in data:
        out["root_squash"] = data["RootSquash"]
    if "NoSquashNids" in data:
        import aws_sdk_fsx.types.lustre_no_squash_nids

        out["no_squash_nids"] = (
            aws_sdk_fsx.types.lustre_no_squash_nids.deserialize_aws_json_1_1(
                data["NoSquashNids"]
            )
        )
    return out
