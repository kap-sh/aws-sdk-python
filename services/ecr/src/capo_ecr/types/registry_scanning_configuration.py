"""Generated from Smithy shape ``com.amazonaws.ecr#RegistryScanningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.registry_scanning_rule_list
    import capo_ecr.types.scan_type


class RegistryScanningConfiguration(TypedDict, closed=True):
    scan_type: NotRequired["capo_ecr.types.scan_type.ScanType"]
    """<p>The type of scanning configured for the registry.</p>"""
    rules: NotRequired[
        "capo_ecr.types.registry_scanning_rule_list.RegistryScanningRuleList"
    ]
    """<p>The scanning rules associated with the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryScanningConfiguration) -> dict:
    out: dict = {}
    if "scan_type" in value:
        import capo_ecr.types.scan_type

        out["scanType"] = capo_ecr.types.scan_type.serialize_aws_json_1_1(
            value["scan_type"]
        )
    if "rules" in value:
        import capo_ecr.types.registry_scanning_rule_list

        out["rules"] = (
            capo_ecr.types.registry_scanning_rule_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryScanningConfiguration:
    out: RegistryScanningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scanType") is not None:
        import capo_ecr.types.scan_type

        out["scan_type"] = capo_ecr.types.scan_type.deserialize_aws_json_1_1(
            data["scanType"]
        )
    if data.get("rules") is not None:
        import capo_ecr.types.registry_scanning_rule_list

        out["rules"] = (
            capo_ecr.types.registry_scanning_rule_list.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    return out
