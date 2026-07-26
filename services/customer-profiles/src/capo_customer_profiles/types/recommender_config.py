"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.events_config
    import capo_customer_profiles.types.included_columns
    import capo_customer_profiles.types.inference_config
    import capo_customer_profiles.types.recommender_config_training_frequency_integer


class RecommenderConfig(TypedDict, closed=True):
    events_config: NotRequired[
        "capo_customer_profiles.types.events_config.EventsConfig"
    ]
    """<p>Configuration settings for how the recommender processes and uses events.</p>"""
    training_frequency: NotRequired[
        "capo_customer_profiles.types.recommender_config_training_frequency_integer.RecommenderConfigTrainingFrequencyInteger"
    ]
    """<p>How often the recommender should retrain its model with new data. If set to 0, automatic retraining will not be enabled.</p>"""
    inference_config: NotRequired[
        "capo_customer_profiles.types.inference_config.InferenceConfig"
    ]
    """<p>Configuration settings for how the recommender handles inference requests.</p>"""
    included_columns: NotRequired[
        "capo_customer_profiles.types.included_columns.IncludedColumns"
    ]
    """<p>A map of dataset type to a list of column names to train on. The <code>_webAnalytics</code> and <code>_catalogItem</code> keys are supported. The column names must be a subset of the columns defined in the recommender schema. If not specified, all columns in the schema are used for training. The following columns are always included in training and do not need to be specified: <code>Item.Id</code>, <code>EventTimestamp</code>, and <code>EventType</code> for <code>_webAnalytics</code>; <code>Id</code> for <code>_catalogItem</code>. Mutually exclusive with ExcludedColumns — both cannot be specified in the same request.</p>"""
    excluded_columns: NotRequired[
        "capo_customer_profiles.types.included_columns.IncludedColumns"
    ]
    """<p>A map of dataset type to a list of column names to exclude from training. The <code>_webAnalytics</code> and <code>_catalogItem</code> keys are supported. The column names must be valid columns defined in the recommender schema. All columns in the schema except the listed columns will be used for training. The following columns are mandatory and cannot be excluded: <code>Item.Id</code>, <code>EventTimestamp</code>, and <code>EventType</code> for <code>_webAnalytics</code>; <code>Id</code> for <code>_catalogItem</code>. Mutually exclusive with IncludedColumns — both cannot be specified in the same request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderConfig) -> dict:
    out: dict = {}
    if "events_config" in value:
        import capo_customer_profiles.types.events_config

        out["EventsConfig"] = capo_customer_profiles.types.events_config.serialize_json(
            value["events_config"]
        )
    if "training_frequency" in value:
        out["TrainingFrequency"] = value["training_frequency"]
    if "inference_config" in value:
        import capo_customer_profiles.types.inference_config

        out["InferenceConfig"] = (
            capo_customer_profiles.types.inference_config.serialize_json(
                value["inference_config"]
            )
        )
    if "included_columns" in value:
        import capo_customer_profiles.types.included_columns

        out["IncludedColumns"] = (
            capo_customer_profiles.types.included_columns.serialize_json(
                value["included_columns"]
            )
        )
    if "excluded_columns" in value:
        import capo_customer_profiles.types.included_columns

        out["ExcludedColumns"] = (
            capo_customer_profiles.types.included_columns.serialize_json(
                value["excluded_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommenderConfig:
    out: RecommenderConfig = {}  # type: ignore[typeddict-item]
    if "EventsConfig" in data:
        import capo_customer_profiles.types.events_config

        out["events_config"] = (
            capo_customer_profiles.types.events_config.deserialize_json(
                data["EventsConfig"]
            )
        )
    if "TrainingFrequency" in data:
        out["training_frequency"] = data["TrainingFrequency"]
    if "InferenceConfig" in data:
        import capo_customer_profiles.types.inference_config

        out["inference_config"] = (
            capo_customer_profiles.types.inference_config.deserialize_json(
                data["InferenceConfig"]
            )
        )
    if "IncludedColumns" in data:
        import capo_customer_profiles.types.included_columns

        out["included_columns"] = (
            capo_customer_profiles.types.included_columns.deserialize_json(
                data["IncludedColumns"]
            )
        )
    if "ExcludedColumns" in data:
        import capo_customer_profiles.types.included_columns

        out["excluded_columns"] = (
            capo_customer_profiles.types.included_columns.deserialize_json(
                data["ExcludedColumns"]
            )
        )
    return out
