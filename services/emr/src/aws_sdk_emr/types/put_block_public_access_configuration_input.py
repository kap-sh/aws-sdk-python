"""Generated from Smithy shape ``com.amazonaws.emr#PutBlockPublicAccessConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.block_public_access_configuration


class PutBlockPublicAccessConfigurationInput(TypedDict):
    block_public_access_configuration: NotRequired[
        "aws_sdk_emr.types.block_public_access_configuration.BlockPublicAccessConfiguration"
    ]
    """<p>A configuration for Amazon EMR block public access. The configuration applies to all clusters created in your account for the current Region. The configuration specifies whether block public access is enabled. If block public access is enabled, security groups associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using <code>PermittedPublicSecurityGroupRuleRanges</code> in the <code>BlockPublicAccessConfiguration</code>. By default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can change this by updating <code>BlockPublicSecurityGroupRules</code> to remove the exception.</p> <note> <p>For accounts that created clusters in a Region before November 25, 2019, block public access is disabled by default in that Region. To use this feature, you must manually enable and configure it. For accounts that did not create an Amazon EMR cluster in a Region before this date, block public access is enabled by default in that Region.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutBlockPublicAccessConfigurationInput) -> dict:
    out: dict = {}
    if "block_public_access_configuration" in value:
        import aws_sdk_emr.types.block_public_access_configuration

        out["BlockPublicAccessConfiguration"] = (
            aws_sdk_emr.types.block_public_access_configuration.serialize_aws_json_1_1(
                value["block_public_access_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutBlockPublicAccessConfigurationInput:
    out: PutBlockPublicAccessConfigurationInput = {}  # type: ignore[typeddict-item]
    if "BlockPublicAccessConfiguration" in data:
        import aws_sdk_emr.types.block_public_access_configuration

        out["block_public_access_configuration"] = (
            aws_sdk_emr.types.block_public_access_configuration.deserialize_aws_json_1_1(
                data["BlockPublicAccessConfiguration"]
            )
        )
    return out
