"""Generated from Smithy shape ``com.amazonaws.secretsmanager#FiltersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.filter

FiltersListType: TypeAlias = list["aws_sdk_secrets_manager.types.filter.Filter"]
