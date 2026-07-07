"""Generated from Smithy shape ``com.amazonaws.imagebuilder#FastLaunchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.account_id
    import aws_sdk_imagebuilder.types.boolean
    import aws_sdk_imagebuilder.types.fast_launch_launch_template_specification
    import aws_sdk_imagebuilder.types.fast_launch_snapshot_configuration
    import aws_sdk_imagebuilder.types.max_parallel_launches


class FastLaunchConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_imagebuilder.types.boolean.Boolean"
    """<p>A Boolean that represents the current state of faster launching for the Windows AMI. Set to <code>true</code> to start using Windows faster launching, or <code>false</code> to stop using it.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.fast_launch_snapshot_configuration.FastLaunchSnapshotConfiguration"
    ]
    """<p>Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when faster launching is enabled.</p>"""
    max_parallel_launches: NotRequired[
        "aws_sdk_imagebuilder.types.max_parallel_launches.MaxParallelLaunches"
    ]
    """<p>The maximum number of parallel instances that are launched for creating resources.</p>"""
    launch_template: NotRequired[
        "aws_sdk_imagebuilder.types.fast_launch_launch_template_specification.FastLaunchLaunchTemplateSpecification"
    ]
    """<p>The launch template that the fast-launch enabled Windows AMI uses when it launches Windows instances to create pre-provisioned snapshots.</p>"""
    account_id: NotRequired["aws_sdk_imagebuilder.types.account_id.AccountId"]
    """<p>The owner account ID for the fast-launch enabled Windows AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FastLaunchConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "snapshot_configuration" in value:
        import aws_sdk_imagebuilder.types.fast_launch_snapshot_configuration

        out["snapshotConfiguration"] = (
            aws_sdk_imagebuilder.types.fast_launch_snapshot_configuration.serialize_json(
                value["snapshot_configuration"]
            )
        )
    if "max_parallel_launches" in value:
        out["maxParallelLaunches"] = value["max_parallel_launches"]
    if "launch_template" in value:
        import aws_sdk_imagebuilder.types.fast_launch_launch_template_specification

        out["launchTemplate"] = (
            aws_sdk_imagebuilder.types.fast_launch_launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> FastLaunchConfiguration:
    out: FastLaunchConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "snapshotConfiguration" in data:
        import aws_sdk_imagebuilder.types.fast_launch_snapshot_configuration

        out["snapshot_configuration"] = (
            aws_sdk_imagebuilder.types.fast_launch_snapshot_configuration.deserialize_json(
                data["snapshotConfiguration"]
            )
        )
    if "maxParallelLaunches" in data:
        out["max_parallel_launches"] = data["maxParallelLaunches"]
    if "launchTemplate" in data:
        import aws_sdk_imagebuilder.types.fast_launch_launch_template_specification

        out["launch_template"] = (
            aws_sdk_imagebuilder.types.fast_launch_launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
