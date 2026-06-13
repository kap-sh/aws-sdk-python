"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargetForms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscription_target_form

SubscriptionTargetForms: TypeAlias = list[
    "aws_sdk_datazone.types.subscription_target_form.SubscriptionTargetForm"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargetForms) -> list:
    import aws_sdk_datazone.types.subscription_target_form

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.subscription_target_form.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriptionTargetForms:
    import aws_sdk_datazone.types.subscription_target_form

    out: SubscriptionTargetForms = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.subscription_target_form.deserialize_json(item)
        )
    return out
