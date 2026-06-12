"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceScoresFilters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_name_filter


class ConformancePackComplianceScoresFilters(TypedDict):
    conformance_pack_names: "aws_sdk_config_service.types.conformance_pack_name_filter.ConformancePackNameFilter"
    """<p>The names of the conformance packs whose compliance scores you want to include in the conformance pack compliance score result set. You can include up to 25 conformance packs in the <code>ConformancePackNames</code> array of strings, each with a character limit of 256 characters for the conformance pack name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceScoresFilters) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.conformance_pack_name_filter

    out["ConformancePackNames"] = (
        aws_sdk_config_service.types.conformance_pack_name_filter.serialize_aws_json_1_1(
            value["conformance_pack_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackComplianceScoresFilters:
    out: ConformancePackComplianceScoresFilters = {}  # type: ignore[typeddict-item]
    if "ConformancePackNames" in data:
        import aws_sdk_config_service.types.conformance_pack_name_filter

        out["conformance_pack_names"] = (
            aws_sdk_config_service.types.conformance_pack_name_filter.deserialize_aws_json_1_1(
                data["ConformancePackNames"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackComplianceScoresFilters.conformance_pack_names required"
        )
    return out
