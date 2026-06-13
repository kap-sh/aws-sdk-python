"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters_list


class DifferentialPrivacyParameters(TypedDict):
    sensitivity_parameters: "aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters_list.DifferentialPrivacySensitivityParametersList"
    """<p>Provides the sensitivity parameters that you can use to better understand the total amount of noise in query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyParameters) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters_list

    out["sensitivityParameters"] = (
        aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters_list.serialize_json(
            value["sensitivity_parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyParameters:
    out: DifferentialPrivacyParameters = {}  # type: ignore[typeddict-item]
    if "sensitivityParameters" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters_list

        out["sensitivity_parameters"] = (
            aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters_list.deserialize_json(
                data["sensitivityParameters"]
            )
        )
    else:
        raise DeserializationError(
            "DifferentialPrivacyParameters.sensitivity_parameters required"
        )
    return out
