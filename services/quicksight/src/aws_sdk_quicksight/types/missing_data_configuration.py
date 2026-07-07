"""Generated from Smithy shape ``com.amazonaws.quicksight#MissingDataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.missing_data_treatment_option


class MissingDataConfiguration(TypedDict, closed=True):
    treatment_option: NotRequired[
        "aws_sdk_quicksight.types.missing_data_treatment_option.MissingDataTreatmentOption"
    ]
    """<p>The treatment option that determines how missing data should be rendered. Choose from the following options:</p> <ul> <li> <p> <code>INTERPOLATE</code>: Interpolate missing values between the prior and the next known value.</p> </li> <li> <p> <code>SHOW_AS_ZERO</code>: Show missing values as the value <code>0</code>.</p> </li> <li> <p> <code>SHOW_AS_BLANK</code>: Display a blank space when rendering missing data.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingDataConfiguration) -> dict:
    out: dict = {}
    if "treatment_option" in value:
        import aws_sdk_quicksight.types.missing_data_treatment_option

        out["TreatmentOption"] = (
            aws_sdk_quicksight.types.missing_data_treatment_option.serialize_json(
                value["treatment_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> MissingDataConfiguration:
    out: MissingDataConfiguration = {}  # type: ignore[typeddict-item]
    if "TreatmentOption" in data:
        import aws_sdk_quicksight.types.missing_data_treatment_option

        out["treatment_option"] = (
            aws_sdk_quicksight.types.missing_data_treatment_option.deserialize_json(
                data["TreatmentOption"]
            )
        )
    return out
