"""Generated from Smithy shape ``com.amazonaws.athena#ResultReuseByAgeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.age
    import aws_sdk_athena.types.boolean


class ResultReuseByAgeConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_athena.types.boolean.Boolean"
    """<p>True if previous query results can be reused when the query is run; otherwise, false. The default is false.</p>"""
    max_age_in_minutes: NotRequired["aws_sdk_athena.types.age.Age"]
    """<p>Specifies, in minutes, the maximum age of a previous query result that Athena should consider for reuse. The default is 60.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultReuseByAgeConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    if "max_age_in_minutes" in value:
        out["MaxAgeInMinutes"] = value["max_age_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultReuseByAgeConfiguration:
    out: ResultReuseByAgeConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "MaxAgeInMinutes" in data:
        out["max_age_in_minutes"] = data["MaxAgeInMinutes"]
    return out
