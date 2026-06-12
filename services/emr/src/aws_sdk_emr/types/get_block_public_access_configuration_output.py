"""Generated from Smithy shape ``com.amazonaws.emr#GetBlockPublicAccessConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.block_public_access_configuration
    import aws_sdk_emr.types.block_public_access_configuration_metadata


class GetBlockPublicAccessConfigurationOutput(TypedDict):
    block_public_access_configuration: NotRequired[
        "aws_sdk_emr.types.block_public_access_configuration.BlockPublicAccessConfiguration"
    ]
    """<p>A configuration for Amazon EMR block public access. The configuration applies to all clusters created in your account for the current Region. The configuration specifies whether block public access is enabled. If block public access is enabled, security groups associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using <code>PermittedPublicSecurityGroupRuleRanges</code> in the <code>BlockPublicAccessConfiguration</code>. By default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can change this by updating the block public access configuration to remove the exception.</p> <note> <p>For accounts that created clusters in a Region before November 25, 2019, block public access is disabled by default in that Region. To use this feature, you must manually enable and configure it. For accounts that did not create an Amazon EMR cluster in a Region before this date, block public access is enabled by default in that Region.</p> </note>"""
    block_public_access_configuration_metadata: NotRequired[
        "aws_sdk_emr.types.block_public_access_configuration_metadata.BlockPublicAccessConfigurationMetadata"
    ]
    """<p>Properties that describe the Amazon Web Services principal that created the <code>BlockPublicAccessConfiguration</code> using the <code>PutBlockPublicAccessConfiguration</code> action as well as the date and time that the configuration was created. Each time a configuration for block public access is updated, Amazon EMR updates this metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlockPublicAccessConfigurationOutput) -> dict:
    out: dict = {}
    if "block_public_access_configuration" in value:
        import aws_sdk_emr.types.block_public_access_configuration

        out["BlockPublicAccessConfiguration"] = (
            aws_sdk_emr.types.block_public_access_configuration.serialize_aws_json_1_1(
                value["block_public_access_configuration"]
            )
        )
    if "block_public_access_configuration_metadata" in value:
        import aws_sdk_emr.types.block_public_access_configuration_metadata

        out["BlockPublicAccessConfigurationMetadata"] = (
            aws_sdk_emr.types.block_public_access_configuration_metadata.serialize_aws_json_1_1(
                value["block_public_access_configuration_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlockPublicAccessConfigurationOutput:
    out: GetBlockPublicAccessConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "BlockPublicAccessConfiguration" in data:
        import aws_sdk_emr.types.block_public_access_configuration

        out["block_public_access_configuration"] = (
            aws_sdk_emr.types.block_public_access_configuration.deserialize_aws_json_1_1(
                data["BlockPublicAccessConfiguration"]
            )
        )
    if "BlockPublicAccessConfigurationMetadata" in data:
        import aws_sdk_emr.types.block_public_access_configuration_metadata

        out["block_public_access_configuration_metadata"] = (
            aws_sdk_emr.types.block_public_access_configuration_metadata.deserialize_aws_json_1_1(
                data["BlockPublicAccessConfigurationMetadata"]
            )
        )
    return out
