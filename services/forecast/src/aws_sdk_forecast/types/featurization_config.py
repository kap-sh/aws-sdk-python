"""Generated from Smithy shape ``com.amazonaws.forecast#FeaturizationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.featurizations
    import aws_sdk_forecast.types.forecast_dimensions
    import aws_sdk_forecast.types.frequency


class FeaturizationConfig(TypedDict):
    forecast_frequency: "aws_sdk_forecast.types.frequency.Frequency"
    """<p>The frequency of predictions in a forecast.</p> <p>Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, \"1D\" indicates every day and \"15min\" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:</p> <ul> <li> <p>Minute - 1-59</p> </li> <li> <p>Hour - 1-23</p> </li> <li> <p>Day - 1-6</p> </li> <li> <p>Week - 1-4</p> </li> <li> <p>Month - 1-11</p> </li> <li> <p>Year - 1</p> </li> </ul> <p>Thus, if you want every other week forecasts, specify \"2W\". Or, if you want quarterly forecasts, you specify \"3M\".</p> <p>The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset frequency.</p> <p>When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the TARGET_TIME_SERIES dataset frequency.</p>"""
    forecast_dimensions: NotRequired[
        "aws_sdk_forecast.types.forecast_dimensions.ForecastDimensions"
    ]
    """<p>An array of dimension (field) names that specify how to group the generated forecast.</p> <p>For example, suppose that you are generating a forecast for item sales across all of your stores, and your dataset contains a <code>store_id</code> field. If you want the sales forecast for each item by store, you would specify <code>store_id</code> as the dimension.</p> <p>All forecast dimensions specified in the <code>TARGET_TIME_SERIES</code> dataset don't need to be specified in the <code>CreatePredictor</code> request. All forecast dimensions specified in the <code>RELATED_TIME_SERIES</code> dataset must be specified in the <code>CreatePredictor</code> request.</p>"""
    featurizations: NotRequired["aws_sdk_forecast.types.featurizations.Featurizations"]
    """<p>An array of featurization (transformation) information for the fields of a dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturizationConfig) -> dict:
    out: dict = {}
    out["ForecastFrequency"] = value["forecast_frequency"]
    if "forecast_dimensions" in value:
        import aws_sdk_forecast.types.forecast_dimensions

        out["ForecastDimensions"] = (
            aws_sdk_forecast.types.forecast_dimensions.serialize_aws_json_1_1(
                value["forecast_dimensions"]
            )
        )
    if "featurizations" in value:
        import aws_sdk_forecast.types.featurizations

        out["Featurizations"] = (
            aws_sdk_forecast.types.featurizations.serialize_aws_json_1_1(
                value["featurizations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturizationConfig:
    out: FeaturizationConfig = {}  # type: ignore[typeddict-item]
    if "ForecastFrequency" in data:
        out["forecast_frequency"] = data["ForecastFrequency"]
    else:
        raise DeserializationError("FeaturizationConfig.forecast_frequency required")
    if "ForecastDimensions" in data:
        import aws_sdk_forecast.types.forecast_dimensions

        out["forecast_dimensions"] = (
            aws_sdk_forecast.types.forecast_dimensions.deserialize_aws_json_1_1(
                data["ForecastDimensions"]
            )
        )
    if "Featurizations" in data:
        import aws_sdk_forecast.types.featurizations

        out["featurizations"] = (
            aws_sdk_forecast.types.featurizations.deserialize_aws_json_1_1(
                data["Featurizations"]
            )
        )
    return out
