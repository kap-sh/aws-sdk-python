"""Generated from Smithy shape ``com.amazonaws.guardduty#UnprocessedDataSourcesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.malware_protection_configuration_result


class UnprocessedDataSourcesResult(TypedDict):
    malware_protection: NotRequired[
        "aws_sdk_guardduty.types.malware_protection_configuration_result.MalwareProtectionConfigurationResult"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedDataSourcesResult) -> dict:
    out: dict = {}
    if "malware_protection" in value:
        import aws_sdk_guardduty.types.malware_protection_configuration_result

        out["malwareProtection"] = (
            aws_sdk_guardduty.types.malware_protection_configuration_result.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> UnprocessedDataSourcesResult:
    out: UnprocessedDataSourcesResult = {}  # type: ignore[typeddict-item]
    if "malwareProtection" in data:
        import aws_sdk_guardduty.types.malware_protection_configuration_result

        out["malware_protection"] = (
            aws_sdk_guardduty.types.malware_protection_configuration_result.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
