"""Generated from Smithy shape ``com.amazonaws.ecr#PutRegistryScanningConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_scanning_rule_list
    import aws_sdk_ecr.types.scan_type


class PutRegistryScanningConfigurationRequest(TypedDict, closed=True):
    scan_type: NotRequired["aws_sdk_ecr.types.scan_type.ScanType"]
    """<p>The scanning type to set for the registry.</p> <p>When a registry scanning configuration is not defined, by default the <code>BASIC</code> scan type is used. When basic scanning is used, you may specify filters to determine which individual repositories, or all repositories, are scanned when new images are pushed to those repositories. Alternatively, you can do manual scans of images with basic scanning.</p> <p>When the <code>ENHANCED</code> scan type is set, Amazon Inspector provides automated vulnerability scanning. You may choose between continuous scanning or scan on push and you may specify filters to determine which individual repositories, or all repositories, are scanned.</p>"""
    rules: NotRequired[
        "aws_sdk_ecr.types.registry_scanning_rule_list.RegistryScanningRuleList"
    ]
    """<p>The scanning rules to use for the registry. A scanning rule is used to determine which repository filters are used and at what frequency scanning will occur.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRegistryScanningConfigurationRequest) -> dict:
    out: dict = {}
    if "scan_type" in value:
        import aws_sdk_ecr.types.scan_type

        out["scanType"] = aws_sdk_ecr.types.scan_type.serialize_aws_json_1_1(
            value["scan_type"]
        )
    if "rules" in value:
        import aws_sdk_ecr.types.registry_scanning_rule_list

        out["rules"] = (
            aws_sdk_ecr.types.registry_scanning_rule_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRegistryScanningConfigurationRequest:
    out: PutRegistryScanningConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scanType" in data:
        import aws_sdk_ecr.types.scan_type

        out["scan_type"] = aws_sdk_ecr.types.scan_type.deserialize_aws_json_1_1(
            data["scanType"]
        )
    if "rules" in data:
        import aws_sdk_ecr.types.registry_scanning_rule_list

        out["rules"] = (
            aws_sdk_ecr.types.registry_scanning_rule_list.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    return out
