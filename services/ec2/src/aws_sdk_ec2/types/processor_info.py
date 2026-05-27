"""Generated from Smithy shape ``com.amazonaws.ec2#ProcessorInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type_list
    import aws_sdk_ec2.types.cpu_manufacturer_name
    import aws_sdk_ec2.types.processor_sustained_clock_speed
    import aws_sdk_ec2.types.supported_additional_processor_feature_list


class ProcessorInfo(TypedDict):
    supported_architectures: NotRequired[
        "aws_sdk_ec2.types.architecture_type_list.ArchitectureTypeList"
    ]
    """<p>The architectures supported by the instance type.</p>"""
    sustained_clock_speed_in_ghz: NotRequired[
        "aws_sdk_ec2.types.processor_sustained_clock_speed.ProcessorSustainedClockSpeed"
    ]
    """<p>The speed of the processor, in GHz.</p>"""
    supported_features: NotRequired[
        "aws_sdk_ec2.types.supported_additional_processor_feature_list.SupportedAdditionalProcessorFeatureList"
    ]
    """<p>Indicates whether the instance type supports AMD SEV-SNP. If the request returns <code>amd-sev-snp</code>, AMD SEV-SNP is supported. Otherwise, it is not supported. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html\"> AMD SEV-SNP</a>.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.cpu_manufacturer_name.CpuManufacturerName"
    ]
    """<p>The manufacturer of the processor.</p>"""
