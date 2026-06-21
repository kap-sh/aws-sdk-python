"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Template``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the type of the aggregation templates in the aggregation configuration. Valid values include API_ACTIVITY, RESOURCE_ACCESS and USER_ACTIONS.</p>"""
Template: TypeAlias = Literal[
    "API_ACTIVITY",
    "RESOURCE_ACCESS",
    "USER_ACTIONS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Template) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Template:
    return cast(Template, data)
