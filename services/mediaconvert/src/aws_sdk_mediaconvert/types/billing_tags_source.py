"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BillingTagsSource``."""

from typing import Literal, TypeAlias, cast

"""The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up."""
BillingTagsSource: TypeAlias = Literal[
    "QUEUE",
    "PRESET",
    "JOB_TEMPLATE",
    "JOB",
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingTagsSource) -> str:
    return value


def deserialize_json(data: str) -> BillingTagsSource:
    return cast(BillingTagsSource, data)
