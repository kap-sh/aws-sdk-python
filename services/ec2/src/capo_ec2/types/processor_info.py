"""Generated from Smithy shape ``com.amazonaws.ec2#ProcessorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.architecture_type_list
    import capo_ec2.types.cpu_manufacturer_name
    import capo_ec2.types.processor_sustained_clock_speed
    import capo_ec2.types.supported_additional_processor_feature_list


class ProcessorInfo(TypedDict, closed=True):
    supported_architectures: NotRequired[
        "capo_ec2.types.architecture_type_list.ArchitectureTypeList"
    ]
    """<p>The architectures supported by the instance type.</p>"""
    sustained_clock_speed_in_ghz: NotRequired[
        "capo_ec2.types.processor_sustained_clock_speed.ProcessorSustainedClockSpeed"
    ]
    """<p>The speed of the processor, in GHz.</p>"""
    supported_features: NotRequired[
        "capo_ec2.types.supported_additional_processor_feature_list.SupportedAdditionalProcessorFeatureList"
    ]
    r"""<p>Indicates whether the instance type supports AMD SEV-SNP. If the request returns <code>amd-sev-snp</code>, AMD SEV-SNP is supported. Otherwise, it is not supported. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html\"> AMD SEV-SNP</a>.</p>"""
    manufacturer: NotRequired[
        "capo_ec2.types.cpu_manufacturer_name.CpuManufacturerName"
    ]
    """<p>The manufacturer of the processor.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProcessorInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "supported_architectures" in value:
        import capo_ec2.types.architecture_type_list

        capo_ec2.types.architecture_type_list.serialize_ec2_query(
            value["supported_architectures"], pairs, f"{prefix}.SupportedArchitectures"
        )
    if "sustained_clock_speed_in_ghz" in value:
        pairs.append(
            (
                f"{prefix}.SustainedClockSpeedInGhz",
                str(value["sustained_clock_speed_in_ghz"]),
            )
        )
    if "supported_features" in value:
        import capo_ec2.types.supported_additional_processor_feature_list

        capo_ec2.types.supported_additional_processor_feature_list.serialize_ec2_query(
            value["supported_features"], pairs, f"{prefix}.SupportedFeatures"
        )
    if "manufacturer" in value:
        pairs.append((f"{prefix}.Manufacturer", str(value["manufacturer"])))


def deserialize_ec2_query(el: Element) -> ProcessorInfo:
    out: ProcessorInfo = {}  # type: ignore[typeddict-item]
    if el.find("SupportedArchitectures") is not None:
        import capo_ec2.types.architecture_type_list

        out["supported_architectures"] = (
            capo_ec2.types.architecture_type_list.deserialize_ec2_query(
                el, "SupportedArchitectures"
            )
        )
    child_sustained_clock_speed_in_ghz = el.find("SustainedClockSpeedInGhz")
    if child_sustained_clock_speed_in_ghz is not None:
        out["sustained_clock_speed_in_ghz"] = float(
            child_sustained_clock_speed_in_ghz.text or ""
        )
    if el.find("SupportedFeatures") is not None:
        import capo_ec2.types.supported_additional_processor_feature_list

        out["supported_features"] = (
            capo_ec2.types.supported_additional_processor_feature_list.deserialize_ec2_query(
                el, "SupportedFeatures"
            )
        )
    child_manufacturer = el.find("Manufacturer")
    if child_manufacturer is not None:
        out["manufacturer"] = str(child_manufacturer.text or "")
    return out
