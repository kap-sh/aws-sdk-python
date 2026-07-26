"""Generated from Smithy shape ``com.amazonaws.machinelearning#SortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>The sort order specified in a listing condition. Possible values include the following:</p> <ul> <li> <p> <code>asc</code> - Present the information in ascending order (from A-Z).</p> </li> <li> <p> <code>dsc</code> - Present the information in descending order (from Z-A).</p> </li> </ul>"""
SortOrder: TypeAlias = Literal[
    "asc",
    "dsc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrder:
    return cast(SortOrder, data)
