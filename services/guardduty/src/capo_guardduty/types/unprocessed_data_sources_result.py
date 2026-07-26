"""Generated from Smithy shape ``com.amazonaws.guardduty#UnprocessedDataSourcesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.malware_protection_configuration_result


class UnprocessedDataSourcesResult(TypedDict, closed=True):
    malware_protection: NotRequired[
        "capo_guardduty.types.malware_protection_configuration_result.MalwareProtectionConfigurationResult"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedDataSourcesResult) -> dict:
    out: dict = {}
    if "malware_protection" in value:
        import capo_guardduty.types.malware_protection_configuration_result

        out["malwareProtection"] = (
            capo_guardduty.types.malware_protection_configuration_result.serialize_json(
                value["malware_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> UnprocessedDataSourcesResult:
    out: UnprocessedDataSourcesResult = {}  # type: ignore[typeddict-item]
    if "malwareProtection" in data:
        import capo_guardduty.types.malware_protection_configuration_result

        out["malware_protection"] = (
            capo_guardduty.types.malware_protection_configuration_result.deserialize_json(
                data["malwareProtection"]
            )
        )
    return out
