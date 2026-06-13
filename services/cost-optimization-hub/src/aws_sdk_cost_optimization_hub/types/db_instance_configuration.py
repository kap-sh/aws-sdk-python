"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#DbInstanceConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DbInstanceConfiguration(TypedDict):
    db_instance_class: NotRequired["str"]
    """<p>The DB instance class of the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbInstanceConfiguration) -> dict:
    out: dict = {}
    if "db_instance_class" in value:
        out["dbInstanceClass"] = value["db_instance_class"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbInstanceConfiguration:
    out: DbInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "dbInstanceClass" in data:
        out["db_instance_class"] = data["dbInstanceClass"]
    return out
