"""Generated from Smithy shape ``com.amazonaws.machinelearning#DataSourceFilterVariable``."""

from typing import Literal, TypeAlias, cast

"""<p>A list of the variables to use in searching or filtering <code>DataSource</code>.</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to <code>DataSource</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to <code>DataSource</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of <code>DataSource</code> <code>Name</code>.</p> </li> <li> <p> <code>DataUri</code> - Sets the search criteria to the URI of data files used to create the <code>DataSource</code>. The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked the <code>DataSource</code> creation.</p> </li> </ul> <p> <b>Note:</b> The variable names should match the variable names in the <code>DataSource</code>.</p>"""
DataSourceFilterVariable: TypeAlias = Literal[
    "CreatedAt",
    "LastUpdatedAt",
    "Status",
    "Name",
    "DataLocationS3",
    "IAMUser",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceFilterVariable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSourceFilterVariable:
    return cast(DataSourceFilterVariable, data)
