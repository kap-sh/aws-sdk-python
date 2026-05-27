"""Generated from Smithy shape ``com.amazonaws.ec2#ThroughResourcesStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.through_resources_statement

ThroughResourcesStatementList: TypeAlias = list[
    "aws_sdk_ec2.types.through_resources_statement.ThroughResourcesStatement"
]
